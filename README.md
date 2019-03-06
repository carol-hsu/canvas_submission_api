# Canvas API for score submission

For TAs easily submit scores to Canvas
Before using the script, you will need **Canvas access token**, **course ID**, **assignment ID** and **student ID**.

## Procedures
- Get your access token

1. Go to canvas, click left side bannar and go to your account setting. 
![get_token_0][GetToken0]

2. In integration part, click "New Access Token" to add a new token. Type a label for it, and set a expiration date. **Be careful: it is not recommended to set token a long time. You may increase the token leaking danger**. The best way is, when you need one, you generate one for single day only.
![get_token_1][GetToken1]

3. Copy the token, you will need it for the API calls. **Caution: do not share it to anyone or spread it in public**.
![get_token_2][GetToken2]

- Get course id

Query every course by API with your token, you can find the course id you want.
```
curl -H 'Authorization: Bearer YOUR_TOKEN' https://gatech.instructure.com/api/v1/courses/
```

Or, you can use [Chrome ARC](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo?hl=zh-TW)
![get_course_id_0][GetCourseId0]

Find the course you want, the `id` in the same JSON object is the course id. Copy it, you will need it.
![get_course_id_1][GetCourseId1]

- Get assignment id

- Get all students' unique id
- Prepare your score file and modify the scripts
- You can also send out comments at the same time

[GetToken0]: https://github.gatech.edu/khsu38/canvas_submission_api/blob/master/figs/get_token_0.png
[GetToken1]: https://github.gatech.edu/khsu38/canvas_submission_api/blob/master/figs/get_token_1.png
[GetToken2]: https://github.gatech.edu/khsu38/canvas_submission_api/blob/master/figs/get_token_2.png
[GetCourseId0]: https://github.gatech.edu/khsu38/canvas_submission_api/blob/master/figs/get_course_id_0.png
[GetCourseId1]: https://github.gatech.edu/khsu38/canvas_submission_api/blob/master/figs/get_course_id_1.png

