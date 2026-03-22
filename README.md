# Online-Cricket-Highlight-System
PROJECT DESCRIPTION:
	This project simulates a real-time cricket highlight generation system similar to those used in live TV broadcasting. The system processes ball-by-ball match data and intelligently selects only the most impactful moments instead of displaying the entire match.
A multi-factor rule engine is used, incorporating:
•	Event importance (SIX, FOUR, WICKET)
•	Match context (runs needed, balls left)
•	Player importance
•	Momentum detection
•	Audience excitement
KEY FEATURES:
•	Real-time highlight simulation
•	Intelligent rule-based decision engine
•	Context-aware (pressure & match situation)
•	Momentum detection (streaks & collapses)
•	Excitement-based filtering
•	Live dashboard using Streamlit
•	Analytics visualization
SYSTEM ARCHITECTURE:
The system is divided into four layers:
1.	Data Layer - Simulated match data (Excel)
2.	Processing Layer - Rule engine computes highlight scores
3.	Networking Layer - JSON used for real-time data transfer
4.	Application Layer - Streamlit dashboard for visualization
Data Layer Implementation 
	In this project, an Excel dataset is used to simulate real-time cricket match data instead of direct hardware sensor integration.
Reason:
	Physical sensors (e.g., IoT devices, ball tracking systems) were not available during development.

KEY CHALLENGES SOLVED:
•	Avoiding excessive highlights 
•	Balancing SIX, FOUR, WICKET 
•	Handling match pressure scenarios 
•	Preventing repetitive events 
•	Simulating real-time streaming 
FUTURE SCOPE:
•	Integration with real IoT sensors 
•	AI/ML-based highlight prediction 
•	Video clip generation 
•	Audio/commentary generation 
•	Cloud-based streaming system 





