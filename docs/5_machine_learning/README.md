# Session 5
How to use IoT Analytics Dataset to train a machine learning model?

## Architecture

In this training session, we will create a notebook instance to train a machine learning model with existing dataset in IoT analytics:
![](img/architecture.png)

## Notebooks
In this section, we will create a Notebook instance (SageMaker) to train a machine learning model with existing dataset in IoT analytics :
![](img/architecture_sagemaker.png)

### Create a Notebook instancce

1. Open the AWS IoT Analytics console.
![](img/iot_analytics_service.png)

1. __Create Notebook__
![](img/iot_notebook_create_1.png)

1. __Blank Notebook__
![](img/iot_notebook_create_2.png)

1. Enter a Name for your notebook. For example, `cxp_insa_tp_iot_notebook` select `cxp_insa_tp_iot_dataset` as __dataset source__ then __Create new__ notebook instance.
![](img/iot_notebook_create_3.png)

1. Enter a Name for your notebook instance. For example, `cxp-insa-tp-iot-notebook-instance` select `ml.m4.xlarge` as __Instance type__ then select `cxp-insa-tp-iot-notebook-role` as role.
![](img/iot_notebook_create_4.png)

1. Notebook instance will be `Pending` during about 5-10 minutes.
![](img/iot_notebook_create_5.png)

1. Select notebook instance `cxp-insa-tp-iot-notebook-instance`.
![](img/iot_notebook_create_6.png)

1. __Create Notebok__.
![](img/iot_notebook_create_7.png)

### Upload .ipynb file

1. __Open in Jupyter__.
![](img/iot_notebook_create_8.png)

1. __Shutdown__ generated notebook.
![](img/iot_notebook_1.png)
![](img/iot_notebook_2.png)

1. Upload .ipynb file.
![](img/iot_notebook_3.png)