# AWS Cloud Cost Optimization - Identifying Stale Resources
   ![Alt text](https://miro.medium.com/v2/resize:fit:720/format:webp/1*Kx0MunAnmkGYN-4AdXF2HQ.png)
## Identifying Stale EBS Snapshots

### Description:

The Lambda function automates the process of identifying and deleting stale EBS snapshots to optimize storage costs. It begins by fetching all EBS snapshots owned by the same AWS account ('self') and retrieves a list of active EC2 instances, including both running and stopped instances.

For each snapshot, the function checks if there is an associated volume and, if so, verifies whether the volume is linked to any of the active EC2 instances. If the volume is not associated with any active instance, the snapshot is considered stale.

Upon identifying a stale snapshot, the function proceeds to delete it. This process helps in managing and reducing unnecessary storage expenses by ensuring that only relevant snapshots are retained.

To automate this cleanup process, the Lambda function is scheduled to run at regular intervals using Amazon CloudWatch Events. CloudWatch triggers the Lambda function automatically based on the defined schedule, ensuring regular identification and deletion of stale snapshots.

we'll create a Lambda function that identifies EBS snapshots that are no longer associated with any active EC2 instance and deletes them to save on storage costs.

