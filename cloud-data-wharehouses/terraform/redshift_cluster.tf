resource "aws_redshift_cluster" "default" {
  cluster_identifier = "my-redshift-cluster"
  database_name      = "mydb"
  master_username    = "dend"
  master_password    = "${var.AWS_REDSHIFT_PASSWORD}"
  node_type          = "dc2.large"
  cluster_type       = "single-node"
}

          [--db-name <value>]
          --cluster-identifier <value>
          [--cluster-type <value>]
          --node-type <value>
          --master-username <value>
          --master-user-password <value>
          [--cluster-security-groups <value>]
          [--vpc-security-group-ids <value>]
          [--cluster-subnet-group-name <value>]
          [--availability-zone <value>]
          [--preferred-maintenance-window <value>]
          [--cluster-parameter-group-name <value>]
          [--automated-snapshot-retention-period <value>]
          [--manual-snapshot-retention-period <value>]
          [--port <value>]
          [--cluster-version <value>]
          [--allow-version-upgrade | --no-allow-version-upgrade]
          [--number-of-nodes <value>]
          [--publicly-accessible | --no-publicly-accessible]
          [--encrypted | --no-encrypted]
          [--hsm-client-certificate-identifier <value>]
          [--hsm-configuration-identifier <value>]
          [--elastic-ip <value>]
          [--tags <value>]
          [--kms-key-id <value>]
          [--enhanced-vpc-routing | --no-enhanced-vpc-routing]
          [--additional-info <value>]
          [--iam-roles <value>]
          [--maintenance-track-name <value>]
          [--snapshot-schedule-identifier <value>]
          [--cli-input-json <value>]
          [--generate-cli-skeleton <value>]
