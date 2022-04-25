from flask import request, current_app, jsonify
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session
from datetime import datetime
import re

from app.models.leads_model import Leads

def verify_phone(data: dict):
  regex = r"(\(\d{2}\))(\d{5}\-\d{4})"
  phone_verification = re.fullmatch(regex, data["phone"])

  if not phone_verification:
    raise ValueError

def verify_type(data: dict):
    for value in list(data.values()):
      if type(value) != str:
        raise TypeError


def create_lead():
    data = request.get_json()
    session: Session = current_app.db.session

    try:
      verify_type(data)
      verify_phone(data)

      new_data = {
      "name": data["name"], 
      "email": data["email"],
      "phone": data["phone"],
      }

      lead = Leads(**new_data)
      session.add(lead)
      session.commit()

      return jsonify(lead), 201

    except IntegrityError:
      return jsonify(erro= "lead com esse número ou email já cadastrado"), 409
    except ValueError: 
      return jsonify(erro= "Telefone obrigatoriamente no formato (xx)xxxxx-xxxx."), 400
    except TypeError:
      return jsonify(erro= "Todos os valores enviados devem ser do tipo string"), 400
    except KeyError:
      return {
               "error": "chave(s) incorreta(s)",
               "permitidas": [
               "name",
               "email",
               "phone"
               ],
               "recebidas": list(data.keys())
            }, 400


def update_lead():
    data = request.get_json()
    session: Session = current_app.db.session
    base_query = session.query(Leads)

    try:
      verify_type(data)

      email = data["email"]
      print(email)
      lead = base_query.filter_by(email=email).one()
      print(lead)

      setattr(lead, "visits",( lead.__dict__["visits"] + 1))
      setattr(lead, "last_visit", datetime.now())

      session.add(lead)
      session.commit()

      return "", 204

    except NoResultFound:
      return jsonify(erro= "Nenhum dado encontrado"), 404
    except TypeError:
      return jsonify(erro= "Todos os valores enviados devem ser do tipo string"), 400
    except KeyError:
      return {
              "error": "chave incorreta",
              "permitida": [
              "email"
              ],
              "recebida(s)": list(data.keys())
          }, 400


def delete_lead():
    data = request.get_json()
    session: Session = current_app.db.session
    base_query = session.query(Leads)

    try:
      verify_type(data)
      
      email = data["email"]
      lead = base_query.filter_by(email=email).one()

      session.delete(lead)
      session.commit()

      return "", 204

    except NoResultFound:
      return jsonify(erro= "Nenhum dado encontrado"), 404
    except TypeError:
      return jsonify(erro= "Todos os valores enviados devem ser do tipo string"), 400
    except KeyError:
        return {
               "error": "chave incorreta",
               "permitida": [
               "email"
               ],
               "recebida(s)": list(data.keys())
            }, 400

def get_leads():
    session: Session = current_app.db.session
    base_query = session.query(Leads)

    leads = base_query.order_by(desc(Leads.visits)).all()

    if not leads:
      return jsonify(erro= "Nenhum dado encontrado"), 404

    return jsonify(leads), 200

