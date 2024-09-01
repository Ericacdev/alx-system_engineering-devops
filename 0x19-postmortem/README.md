Issue Summary

On Aug 25, 2024, from 10:45 to 12:15 SAST, our customer support portal experienced a 90-minute outage that affected 70% of users attempting to submit support tickets. Users encountered error messages when submitting forms, and many were unable to log in. The root cause was a misconfigured database connection pool, which led to an exhaustion of available connections and ultimately brought the service to a halt.

Timeline

10:45 SAST: Monitoring alerts triggered, indicating a sudden spike in database query failures.
10:50 SAST: On-call engineer investigates and initially suspects a network issue causing connectivity problems to the database.
11:00 SAST: Network team checks for latency or packet loss but finds no anomalies.
11:10 SAST: A customer complaint is received, reporting issues with submitting support tickets.
11:15 SAST: Investigation shifts to the application layer, checking for any recent deployments that could have introduced bugs.
11:30 SAST: Misleading logs suggest a potential issue with application code related to form validation.
11:45 SAST: Incident escalated to the database administration team after noticing recurring “connection pool exhausted” errors in the logs.
12:00 SAST: Database configuration is reviewed, revealing that the connection pool was not properly scaled for increased user load.
12:05 SAST: Database connection pool settings are updated and the database is restarted to clear existing connections.
12:15 SAST: Service is fully restored, and the incident is marked as resolved.

Root Cause and Resolution

The root cause of the outage was an improperly configured database connection pool. The application was set to a default connection pool size that was insufficient for the spike in user activity on Aug 25. As user requests exceeded the available connections, the application began timing out, leading to errors and failed form submissions.

To resolve the issue, the connection pool size was increased to accommodate the higher load, and the database was restarted to flush out the exhausted connections. This allowed the service to return to normal operations.

Corrective and Preventative Measures

To prevent similar issues in the future, the following steps will be taken:

1. Optimize Connection Pool Settings: Review and adjust the default database connection pool settings to better handle high traffic volumes.
2. Implement Dynamic Scaling: Introduce dynamic scaling for the database connection pool based on real-time traffic to prevent exhaustion during peak periods.
3. Enhance Monitoring: Set up additional monitoring alerts specifically for database connection pool utilization to detect and address issues before they lead to service outages.
4. Conduct Load Testing: Perform regular load testing on the customer support portal to ensure the system can handle expected traffic increases.
5. Improve Incident Response Procedures :
Update the incident response playbook to include database connection pool checks as a standard step when troubleshooting application-level issues.

By implementing these measures, we aim to improve system resilience and reduce the risk of similar outages in the future.
