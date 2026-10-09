from typing import Dict, Set

class FastSpatialGrid:
    """
    High-performance 2D spatial hash grid using bit-packed integer keys
    to avoid garbage collection pressure from tuple generation in frames.
    """
    def __init__(self, cell_size: int = 64):
        self.cell_size = cell_size
        self.grid: Dict[int, Set[int]] = {}
        self.entity_locations: Dict[int, int] = {}

    def _pack_key(self, x: float, y: float) -> int:
        # Translate coordinates to prevent negative integer issues in shift operations
        cx = (int(x) // self.cell_size) + 32768
        cy = (int(y) // self.cell_size) + 32768
        return (cx << 16) | cy

    def update(self, entity_id: int, x: float, y: float) -> None:
        key = self._pack_key(x, y)
        old_key = self.entity_locations.get(entity_id)
        
        if old_key == key:
            return
            
        if old_key is not None:
            cell = self.grid.get(old_key)
            if cell:
                cell.discard(entity_id)
                if not cell:
                    del self.grid[old_key]
                    
        self.entity_locations[entity_id] = key
        if key not in self.grid:
            self.grid[key] = {entity_id}
        else:
            self.grid[key].add(entity_id)

    def remove(self, entity_id: int) -> None:
        old_key = self.entity_locations.pop(entity_id, None)
        if old_key is not None:
            cell = self.grid.get(old_key)
            if cell:
                cell.discard(entity_id)
                if not cell:
                    del self.grid[old_key]

    def get_nearby(self, x: float, y: float, radius: float) -> Set[int]:
        nearby: Set[int] = set()
        cx_min = (int(x - radius) // self.cell_size) + 32768
        cx_max = (int(x + radius) // self.cell_size) + 32768
        cy_min = (int(y - radius) // self.cell_size) + 32768
        cy_max = (int(y + radius) // self.cell_size) + 32768

        for cx in range(cx_min, cx_max + 1):
            cx_shift = cx << 16
            for cy in range(cy_min, cy_max + 1):
                key = cx_shift | cy
                cell = self.grid.get(key)
                if cell:
                    nearby.update(cell)
        return nearby