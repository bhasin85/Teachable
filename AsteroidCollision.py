class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collisions = []
        
        # peek -> -ve, +ve, None
        # asteroid -> -ve, +ve
        
        for asteroid in asteroids:
            self._add(collisions, asteroid)
                
        return collisions
    
    def _add(self, collisions, asteroid):
        if len(collisions) == 0:
            collisions.append(asteroid)
            return

        # last_asteroid:+ve asteroid:-ve -> collision
        if collisions[-1] > 0 and asteroid < 0:
            # check collision
            last_asteroid = collisions.pop()
            if last_asteroid + asteroid == 0:
                # explode both
                return
            elif last_asteroid*last_asteroid > asteroid*asteroid:
                self._add(collisions, last_asteroid)
            else:
                self._add(collisions, asteroid)                
        else:
        # last_asteroid:-ve asteroid:+ve -> no collision
        # last_asteroid:+ve asteroid:+ve -> no collision
        # last_asteroid:-ve asteroid:-ve -> no collision            
            collisions.append(asteroid)
                
