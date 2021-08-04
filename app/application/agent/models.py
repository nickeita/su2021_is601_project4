from . import agent_db


class Agent(agent_db.Model):

    # Data model for real estate agent profile
    __tablename__ = 'Agents'
    agent_id = agent_db.Column(agent_db.Integer, primary_key=True)

    firstname = agent_db.Column(agent_db.String(50), index=False, unique=False, nullable=False)

    lastname = agent_db.Column(agent_db.String(50), index=False, unique=False, nullable=False)

    phone = agent_db.Column(agent_db.String(10), index=False, unique=False, nullable=False)

    email = agent_db.Column(agent_db.String(50), index=False, unique=False, nullable=False)

