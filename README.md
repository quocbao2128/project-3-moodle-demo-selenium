# **project-3-moodle-demo-selenium**

# **Website used for testing:** [Moodle demo](https://school.moodledemo.net/)

# **Tech stacks:**
- [python](https://www.python.org/downloads/)
- [selenium webdriver](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/)
- [pytest](https://pypi.org/project/pytest/)
- [openpyxl](https://pypi.org/project/openpyxl/)


# **Test data file:** `test_data.xlsx`
![google_drive](https://ssl.gstatic.com/images/branding/product/1x/drive_2020q4_48dp.png)[**Google Drive**](https://docs.google.com/spreadsheets/d/1b7RbgUlz37cmoLDspodr4RVmjNMAUm7s/edit?usp=drive_link&ouid=108255664829481892302&rtpof=true&sd=true)

# **How to run:**
## 1. Install [python](https://www.python.org/downloads/) (if not already installed)
![step01](https://github.com/quocbao2128/project-3-moodle-demo-selenium/assets/84076266/005e3b6c-387d-4683-811a-adc7093a01f9)

![step02](https://github-production-user-asset-6210df.s3.amazonaws.com/84076266/287788494-a6005d36-6283-44a8-9df7-4e496802638e.PNG?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20231204%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231204T175825Z&X-Amz-Expires=300&X-Amz-Signature=5db238fb07a24e6d671653b92524fd3d2c5d204648a4fa427e07a6790fb2ff42&X-Amz-SignedHeaders=host&actor_id=84076266&key_id=0&repo_id=726509442)

![step03](https://github-production-user-asset-6210df.s3.amazonaws.com/84076266/287788537-0f8fe877-14f0-454c-8a95-9569bd48ac21.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20231204%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231204T175855Z&X-Amz-Expires=300&X-Amz-Signature=5a0e7982cf4507d9fea772a6216d914cd66b7f3cd624c2439696cf43ff8918d9&X-Amz-SignedHeaders=host&actor_id=84076266&key_id=0&repo_id=726509442)

![step04](https://github-production-user-asset-6210df.s3.amazonaws.com/84076266/287788553-37b59ce6-7f94-4ed6-851b-826a82a1fd79.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20231204%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231204T175917Z&X-Amz-Expires=300&X-Amz-Signature=4eb6d4f44e1bf5e5dba523c510f4af7be83df20bed8590da53007ee014f17134&X-Amz-SignedHeaders=host&actor_id=84076266&key_id=0&repo_id=726509442)

## 2. Install [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download) (if not already installed)

## 3. Clone this repository

## 4. Config pytest in Pycharm
![step05](https://github-production-user-asset-6210df.s3.amazonaws.com/84076266/287791874-39451674-8ddc-4e39-ba83-1947c945049e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20231204%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231204T181221Z&X-Amz-Expires=300&X-Amz-Signature=c25ed239bbc350673e2e7172682cd251848548e0ded02edbb9ecdb3e9f1a779b&X-Amz-SignedHeaders=host&actor_id=84076266&key_id=0&repo_id=726509442)

## 5. Download `test_data.xlsx` from [here](https://docs.google.com/spreadsheets/d/1b7RbgUlz37cmoLDspodr4RVmjNMAUm7s/edit?usp=drive_link&ouid=108255664829481892302&rtpof=true&sd=true), then copy into root project folder (example: `D:\project-3-moodle-demo-selenium\`)
### The directory structure is as follows:
![step06](https://github-production-user-asset-6210df.s3.amazonaws.com/84076266/287795396-26338988-2603-4a2b-9be3-22c81a26d2c9.PNG?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20231204%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231204T182749Z&X-Amz-Expires=300&X-Amz-Signature=15fc36b9c9542ddd18a56d2189fe1d9e14cf3f9d2735f06d49c8829b3dcb9d67&X-Amz-SignedHeaders=host&actor_id=84076266&key_id=0&repo_id=726509442)

## 6. Open a file in the `level_0` folder (or also the `level_1`, `level_2` folder), then click `Run` button

![step07](https://github-production-user-asset-6210df.s3.amazonaws.com/84076266/287797334-e864661b-3f75-4832-bc60-f261aa8e4e75.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20231204%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231204T183658Z&X-Amz-Expires=300&X-Amz-Signature=4a94c2cda0e79d500ba0dc1ca543f41bbb180f4d4858282bf177ff7f69b79b30&X-Amz-SignedHeaders=host&actor_id=84076266&key_id=0&repo_id=726509442)

## 7. Click `Run` tab to observe the running process of the test case. After completion, a summary `report` of the test case running results will appear next to it showing how many test cases `PASSED`/`FAILED` and display errors (if any) as well as the total execution time.

![step08](https://github-production-user-asset-6210df.s3.amazonaws.com/84076266/287801846-ce37e588-e380-4d76-8abd-18df36389f14.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20231204%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231204T185658Z&X-Amz-Expires=300&X-Amz-Signature=0f82bc9fef0b3e6df9fcf6e28afca7c7a963cd1b66d38e848d0c719bf5bd6899&X-Amz-SignedHeaders=host&actor_id=84076266&key_id=0&repo_id=726509442)

The percentage represents the overall progress after running a test case. (For example in the image below: there are 4 test cases, after running test case 1, the overall process is 25% complete).
