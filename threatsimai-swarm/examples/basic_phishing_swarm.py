from core.simulator import AISwarm

if __name__ == "__main__":
    # Custom config override example
    swarm = AISwarm()
    swarm.num_agents = 2000
    swarm.attack_types = ["phishing"]  # Focus only on phishing swarm
    swarm.launch_swarm(duration=45)