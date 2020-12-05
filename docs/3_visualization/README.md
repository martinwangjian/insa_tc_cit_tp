# Session 2
How to visualize data with BI tool?

## Architecture

In this training session, we will add IoT Analytics Dataset and QuickSight to our existing architecture:
![](img/architecture.png)

In preview session, we have published data to AWS IoT Analytics Datastore. In this session, we will visualise a subset of data (IoT Analytics Dataset).

## IoT Analytics Dataset

In this section, we will create a IoT Analytics Dataset:
![](img/architecture_dataset.png)

You retrieve data from a data store by creating a SQL dataset or a container dataset. AWS IoT Analytics can query the data to answer analytical questions. Although a data store is not a database, you use SQL expressions to query the data and produce results that are stored in a data set.

### Create a dedicated S3 bucket for AWS IoT Analytics Dataset
1. Open the S3 console.
![](img/s3_service.png)

1. Create a bucket.
![](img/s3_create_bucket.png)

1. Enter a Name for your bucket. For example, `cxp-insa-tp-iot-analytics-dataset-<your group id>`.
__Note__: __*An Amazon S3 bucket name is globally unique, and the namespace is shared by all AWS accounts. This means that after a bucket is created, the name of that bucket cannot be used by another AWS account in any AWS Region until the bucket is deleted.*__

1. Choose `eu-west-1` as Region and Check `Block all public access` option

1. Keep default options and Create bucket:

### Create an AWS IoT Analytics Dataset
1. Open the AWS IoT Analytics console.
![](img/iot_analytics_service.png)

1. Choose Create a dataset.
![](img/iot_analytics_dataset_create_1.png)

1. Select __SQL__ as __Type__.
![](img/iot_analytics_dataset_create_2.png)

1. Enter a Name for your dataset. For example, `cxp_insa_tp_iot_dataset` select `cxp_insa_tp_iot_datastore` as __datastore source__ .
![](img/iot_analytics_dataset_create_3.png)

1. Enter SQL Query `SELECT date, TemperatureC FROM cxp_insa_tp_iot_datastore` then __Test Query__
![](img/iot_analytics_dataset_create_4.png)

1. You should be able to see __Result preview__, then __Next__
![](img/iot_analytics_dataset_create_5.png)

1. Select __None__ as __Data selection window__
![](img/iot_analytics_dataset_create_6.png)

1. Select __Not scheduled__ as __Frequency__
![](img/iot_analytics_dataset_create_7.png)

1. Select __No rule selected__ as __Data set content delivery rule__ then __Create dataset__
![](img/iot_analytics_dataset_create_8.png)

1. Select your data set and __run now__
![](img/iot_analytics_dataset_create_9.png)

1. Verify that you have data in your data set __content__
![](img/iot_analytics_dataset_create_10.png)

## QuickSight

QuickSight is serverless and can automatically scale to tens of thousands of users without any infrastructure to manage or capacity to plan for. It is also the first BI service to offer pay-per-session pricing, where you only pay when your users access their dashboards or reports, making it cost-effective for large scale deployments.

In this section, we will use QuickSight to visualize data:
![](img/architecture_quicksight.png)

### Prepare QuickSight
1. Open the QuickSight console.
![](img/service_quicksight.png)

1. Enter your email address to create QuickSight subscription.
![](img/quicksight_email.png)

1. Finalyze QuickSight account creation.
![](img/quicksight_welcome.png)

1. Grant QuickSight permission to access IoT Analytics: __Manage QuickSight__>__Security & permissions__>__Add or remove__
![](img/quicksight_manage.png)

1. Select __AWS IoT Analytics__
![](img/quicksight_add_permission.png)

1. Verification
![](img/quicksight_verify_permission.png)

### Create an Analyse

1. Add dataset
![](img/quicksight_add_dataset.png)

1. Select __AWS IoT Analytics__
![](img/quicksight_add_dataset_analytics.png)

1. Select `cxp-insa-tp-iot-analytics-dataset`
![](img/quicksight_add_dataset_analytics_2.png)

1. Finish data set creation
![](img/quicksight_add_dataset_analytics_3.png)

1. Select __Line Chart__ and add `date` as __X axis__
![](img/quicksight_analysis_1.png)

1. Add `temperaturec` as __Y axis__ and select __Average__ as __Aggregate__
![](img/quicksight_analysis_2.png)