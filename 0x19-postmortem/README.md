**Postmortem: Web Stack Outage on May 3rd, 2024**

**Issue Summary:**

Between the hour of 3:00 AM and 5:30 AM on May 3rd, 2024 (UTC), 30% of users encountered slow response times or complete unavailability of our web application due to a misconfigured load balancer.

**Timeline:**

- **3:00 AM:** Issue detected through monitoring alerts indicating high latency.
- **3:05 AM:** Engineering team notified and investigation initiated.
- **3:20 AM:** Initial assumption was a server overload due to increased traffic.
- **3:30 AM:** Load balancer logs reviewed, revealing misconfiguration.
- **4:00 AM:** Misleading investigation paths included checking for database issues and network congestion, which were ruled out.
- **4:15 AM:** Incident escalated to senior engineering team for further troubleshooting.
- **5:00 AM:** Load balancer configuration corrected.
- **5:30 AM:** Services fully restored.

**Root Cause and Resolution:**

- **Root Cause:** Misconfigured load balancer was not distributing traffic evenly among the application servers.
- **Resolution:** Load balancer configuration was adjusted to evenly distribute traffic among servers.

**Corrective and Preventative Measures:**

- **Improvements/Fixes:** Enhance monitoring to detect load balancer misconfigurations. Implement automated checks for load balancer settings.
- **Tasks:**
  - Implement automated load balancer configuration checks by May 15th, 2024.
  - Conduct load testing scenarios to verify load balancer behavior under different traffic loads by June 1st, 2024.
  - Review and update incident response plan to include load balancer misconfiguration scenarios by June 15th, 2024

By addressing these tasks, I  aim to prevent similar outages in the future and improve the overall reliability of our web application.
