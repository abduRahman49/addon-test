from flask import Flask, jsonify, request
from uuid import uuid4


app = Flask(__name__)


@app.route("/transferts/debits/new", methods=['POST'])
def debit_reservation():
    return jsonify({
        "ok": True,
        "code_retour": "ACSP",
        "ref_transaction_participant": uuid4()
    })


@app.route("/transferts/debits/confirmer", methods=['POST'])
def debit_confirmation():
    request_data = request.get_json()
    return jsonify({
        "ok": True,
        "end_to_end_id": request_data.get("end_to_end_id")
    })


@app.route("/transferts/debits/rejeter", methods=['POST'])
def debit_rejet():
    request_data = request.get_json()
    return jsonify({
        "ok": True,
        "end_to_end_id": request_data.get("end_to_end_id")
    })


@app.route("/transferts/credits/new", methods=['POST'])
def credit_reservation():
    return jsonify({
        "ok": True,
        "code_retour": "ACSP",
        "ref_transaction_participant": uuid4()
    })


@app.route("/transferts/credits/confirmer", methods=['POST'])
def credit_confirmation():
    request_data = request.get_json()
    return jsonify({
        "ok": True,
        "end_to_end_id": request_data.get("end_to_end_id")
    })


@app.route("/transferts/credits/rejeter", methods=['POST'])
def credit_rejet():
    request_data = request.get_json()
    return jsonify({
        "ok": True,
        "end_to_end_id": request_data.get("end_to_end_id")
    })


@app.route("/comptes/kyc", methods=['POST'])
def get_kyc():
    return jsonify({
        "resultat_verification": True,
        "raison_rejet": "",
        "compte_client": "562422",
        "type_compte": "CACC",
        "date_ouverture": "2024-01-30",
        "nom_client": "WEBART",
        "nationalite": "CL",
        "denomination_sociale": "WEBART",
        "raison_sociale": "WEBART",
        # "genre": "F",
        "telephone": "+221604908553",
        "ville_client": "West Kennethhaven",
        "adresse_complete": "PSC 9071, Box 3548 APO AA 26487",
        "numero_identification": "042-54-0792",
        "systeme_identification": "TXID",
        # "date_naissance": "1978-04-16",
        # "ville_naissance": "Port Stephanie",
        # "pays_naissance": "GW",
        "pays_residence": "NE",
        "devise": "XOF",
        "type_client": "B",
        "photo": "string"
    })
