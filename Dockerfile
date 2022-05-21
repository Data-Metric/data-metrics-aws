FROM public.ecr.aws/lambda/python:3.9

# Copy function code
RUN  mkdir ${LAMBDA_TASK_ROOT}/data_metric_mf_aws
COPY data_metric_mf_aws ${LAMBDA_TASK_ROOT}/data_metric_mf_aws/
COPY pyproject.toml ${LAMBDA_TASK_ROOT}/

WORKDIR ${LAMBDA_TASK_ROOT}/

RUN ls -lrt

RUN pip install poetry
RUN poetry install

ARG MF_API_KEY
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION

ENV MF_API_KEY $MF_API_KEY
ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]