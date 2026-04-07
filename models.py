from typing import Literal, Optional
from openenv.core.env_server.types import Action, Observation
from pydantic import Field, ConfigDict

class SupportTicketTriageAction(Action):
    """Action for the Sentinel SOC environment."""
    action_type: Literal["investigate", "mitigate", "report", "submit", "start_mission", "search_kb", "update_ticket", "reply", "start_task"] = Field(
        ..., description="The type of action to perform."
    )
    task_level: Optional[Literal["easy", "medium", "hard"]] = Field(
        None, description="Only for start_mission. Selects difficulty."
    )
    search_query: Optional[str] = Field(None, description="Only for investigate. Query Threat Intel / Logs.")
    priority: Optional[Literal["low", "medium", "high", "critical", "urgent"]] = Field(None, description="Only for mitigate. Set incident priority/severity.")
    team: Optional[Literal["billing", "it_support", "product", "hardware", "security", "hr"]] = Field(None, description="Only for mitigate. Route to a specialized response team.")
    status: Optional[Literal["open", "in_progress", "resolved", "escalated"]] = Field(None, description="Only for mitigate. Set incident status.")
    reply_text: Optional[str] = Field(None, description="Only for report. The text summary for the incident report.")
    
    model_config = ConfigDict(extra="ignore")

class SupportTicketTriageObservation(Observation):
    """Observation from the Sentinel SOC environment."""
    current_ticket: str = Field(default="", description="The content of the current security incident / alert.")
    kb_search_results: str = Field(default="", description="Threat intelligence and logs retrieved.")
    ticket_status: str = Field(default="open", description="Current status of the incident.")
    ticket_priority: str = Field(default="unassigned", description="Current severity of the threat.")
    ticket_team: str = Field(default="unassigned", description="Assigned mitigation unit.")
    draft_reply: str = Field(default="", description="The current drafted incident report.")
    system_message: str = Field(default="", description="Feedback or error messages from the system.")
    reward: float = Field(default=0.0, description="The reward obtained in the last step.")
    done: bool = Field(default=False, description="Whether the mission is completed.")
    step_count: int = Field(default=0, description="Current step count in the mission.")
