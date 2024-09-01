**Issue Summary: When Our Database Took a Nap**

On July 25, 2024, from 10:45 to 12:15 SAST, our customer support portal decided to take an unscheduled “power nap,” leaving 70% of our users unable to submit support tickets. Instead of getting help, users were met with error messages and frustration. The culprit? A sneaky memory hog in the database connection pool, which caused the whole system to get groggy and eventually pass out.


**Timeline**

- **10:45 SAST**: Our monitoring system raised the alarm like a fire drill, alerting us to database query failures.
- **10:50 SAST**: The on-call engineer’s first thought: “Must be the network acting up again!”
- **11:00 SAST**: Network team confirms everything is peachy on their end (not a single cable out of place).
- **11:10 SAST**: Customer support chimes in with reports of users getting error messages. Chaos ensues.
- **11:15 SAST**: We start chasing a ghost in the application code, suspecting a form validation issue.
- **11:30 SAST**: After chasing that ghost for a bit, we realized it was a dead end. Oops!
- **11:45 SAST**: The real villain is uncovered—a connection pool that couldn’t handle the heat.
- **12:00 SAST**: We crank up the connection pool size, give the database a quick restart, and the system wakes up, all bright-eyed and bushy-tailed.
- **12:15 SAST**: Services are restored, and we promise to never let the database nap on the job again.

**Root Cause and Resolution**

The root cause was a misconfigured database connection pool that was too small to handle the surge in traffic on July 25. As the pool filled up, the database started struggling, leading to timeouts and error messages. It was like trying to cram an elephant into a Volkswagen Beetle—just not gonna happen!

To fix the issue, we expanded the connection pool to make room for all the traffic, then restarted the database to get rid of the backlog. The system came back to life, and users could once again submit their support tickets without a hitch.

**Corrective and Preventative Measures**

To prevent future “database naps,” we’re taking the following steps:

1. **Increase the Connection Pool Size**: No more trying to fit that elephant into a Beetle—our connection pool is now sized to handle peak traffic.
2. **Add Dynamic Scaling**: We’re giving the connection pool the ability to stretch like elastic, adjusting automatically to traffic demands.
3. **Better Monitoring**: We’ve added new alerts to catch any signs of the database feeling drowsy, so we can take action before it snoozes.
4. **Regular Load Testing**: Like a workout for our database, we’ll be stress-testing regularly to keep it in top shape.
5. **Improve Incident Response**: We’ve updated our playbook to make sure we check the connection pool first next time—no more chasing ghosts!
