# Explanations
---------------
## IAM Policies inheritance
* Policies can be attached in group level (Policy will get applied to every single user part of the group)
* Policy can also be attached to individual user if required (which is called `inline` policies)
* Users also can be part of multiple group (In this case every policies attached in each individual group will also get inherit to users)
* Example: ![alt text](../../content-images/image_11.png)

## How to understand IAM policy
* Example: ![alt text](../../content-images/image_12.png)
* Version: Policy language version (default: 2012-10-17)
* Id: Identifier for the policy (optional)
* Statement: One or more individual statements can be added (required)
* Sid: An identifier of statement
* Effect: Whether the statement allows or denies access (Allow, Deny)
* Principal: account/user/role to which this policy applied to
* Action: list of actions this policy allows or denies
* Resource: list of resources to which the action applied to

# Handson