# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
from flask import Flask
from flask import request
from pony import orm
from .database import to_db, db

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)

VERSION = "0.0.1"
__version__ = VERSION

app = Flask(__name__)


@orm.db_session
@app.route("/dump/", methods=['POST', 'GET', 'PUT'])
def dump_to_db():
    try:
        logger.info("Incoming: {}".format(request.get_json()))
        msg = to_db(request.get_json(force=True))
        db.commit()
        logger.info("Added {}: {id}".format(msg, id=msg.id))
        return "ok: {}".format(msg)
    except Exception as e:
        logger.exception("lel")
        raise
# end def


@app.route("/")
def root():
    return "Ready to take your requests."
# end def
