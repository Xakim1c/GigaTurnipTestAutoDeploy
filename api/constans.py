class TaskStageConstants:
    RANK = 'RA'
    STAGE = 'ST'
    INTEGRATOR = 'IN'
    AUTO_COMPLETE = 'AU'
    PREVIOUS_MANUAL = 'PA'


class CopyFieldConstants:
    USER = 'US'
    CASE = 'CA'


class AutoNotificationConstants:
    FORWARD = 'FW'
    BACKWARD = 'BW'
    LAST_ONE = 'LO'


class FieldsJsonConstants:
    META_QUIZ_SCORE = 'meta_quiz_score'
    META_QUIZ_INCORRECT_QUESTIONS = 'meta_quiz_incorrect_questions'


class ErrorConstants:
    CANNOT_SUBMIT = 'You may not submit this task!'
    TASK_COMPLETED = 'Task is being completed!'
    TASK_ALREADY_COMPLETED = 'Task is already complete!'
    IMPOSSIBLE_ACTION = 'It is impossible to %s task.'
    UNSUPPORTED_TYPE = 'Unsupported \'%s\'.'
    SEND_TO_MODERATORS = 'Please send this message to your moderators.'
    ENTITY_DOESNT_EXIST = '%s %s doesn\'t exist.'
    ENTITY_IS_NOT_IN_CAMPAIGN = '%s is not in the campaign.'