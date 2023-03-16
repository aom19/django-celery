from celery.decorators import task

from .email import send_feedback_email_task

from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@task(name="send_feedback_email_task")
def send_feedback_email_task(name, email, review):
	logger.info("Sent email")
	return send_feedback_email_task(name, email, review)


