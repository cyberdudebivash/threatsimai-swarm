import click
from core.simulator import AISwarm

@click.command()
@click.option('--agents', default=1000, help='Number of swarm agents (default: 1000)')
@click.option('--duration', default=60, help='Attack duration in seconds (default: 60)')
@click.option('--config', default='config/swarm_config.yaml', help='Path to config file')
def run_swarm(agents, duration, config):
    """Launch ThreatSimAI Swarm Edition"""
    click.echo(click.style("ThreatSimAI Swarm Edition v0.1 - CyberdudeBivash Pvt Ltd", fg='cyan', bold=True))
    swarm = AISwarm(config_file=config)
    swarm.num_agents = agents
    swarm.launch_swarm(duration=duration)

if __name__ == '__main__':
    run_swarm()