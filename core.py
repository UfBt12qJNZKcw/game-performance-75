import sys
from typing import List

class Entity:
    __slots__ = ('id', 'x', 'y', 'vx', 'vy', 'active', 'priority')
    
    def __init__(self, entity_id: int, x: float, y: float, vx: float, vy: float):
        self.id = entity_id
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.active = True
        self.priority = 1

class FrameBudgetManager:
    # Optimizes updates by distributing non-critical updates across alternating frames
    def __init__(self):
        self.entities: List[Entity] = []
        self.frame_count = 0

    def register(self, entity: Entity) -> None:
        self.entities.append(entity)

    def update_priorities(self, player_x: float, player_y: float) -> None:
        # Distance-squared check avoids costly square root operations
        for ent in self.entities:
            dx = ent.x - player_x
            dy = ent.y - player_y
            dist_sq = dx * dx + dy * dy
            if dist_sq < 10000.0:
                ent.priority = 1
            elif dist_sq < 90000.0:
                ent.priority = 2
            else:
                ent.priority = 4

    def step(self, dt: float) -> int:
        self.frame_count += 1
        updated_count = 0
        fc = self.frame_count
        
        # Compensate step velocity relative to the update interval priority skipping
        for ent in self.entities:
            if ent.active and (fc % ent.priority == 0):
                ent.x += ent.vx * dt * ent.priority
                ent.y += ent.vy * dt * ent.priority
                updated_count += 1
                
        return updated_count
