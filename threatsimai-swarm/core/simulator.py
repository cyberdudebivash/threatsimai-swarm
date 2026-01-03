import random
import time
import threading
from tqdm import tqdm
import yaml

class SwarmAgent:
    def __init__(self, agent_id, target):
        self.id = agent_id
        self.target = target
        self.alive = True

    def execute_attack(self, attack_type):
        # Simulate network delay + processing
        time.sleep(random.uniform(0.05, 0.3))
        print(f"[AGENT {self.id:04d}] → {attack_type.upper()} on {self.target}")

class AISwarm:
    def __init__(self, config_file="config/swarm_config.yaml"):
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)

        self.num_agents = self.config['swarm']['default_agents']
        self.target = self.config['swarm']['target_network']
        self.attack_types = self.config['attacks']

        self.agents = [SwarmAgent(i, self.target) for i in range(self.num_agents)]

    def launch_swarm(self, duration=None):
        duration = duration or self.config['swarm']['duration_seconds']
        print(f"\n[LAUNCHING AI SWARM] {self.num_agents} agents → {self.target}\n")

        threads = []
        for agent in tqdm(self.agents, desc="Swarm Active", unit="agent"):
            attack = random.choice(self.attack_types)
            t = threading.Thread(target=agent.execute_attack, args=(attack,))
            t.start()
            threads.append(t)

        time.sleep(duration)

        for t in threads:
            t.join()

        print(f"\n[SWARM COMPLETE] Simulated {duration}s attack cycle finished.")

if __name__ == "__main__":
    swarm = AISwarm()
    swarm.launch_swarm()