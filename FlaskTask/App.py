from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory database
finance_data = []

@app.route('/')
def home():
    """Render the homepage."""
    return render_template('home.html')

@app.route('/transactions')
def view_transactions():
    """Render the transactions page."""
    return render_template('transactions.html')

@app.route('/transactions/api', methods=['GET', 'POST'])
def transactions():
    """Handle listing all transactions or adding a new one."""
    if request.method == 'POST':
        # Add a new transaction
        data = request.get_json()
        new_transaction = {
            "id": len(finance_data) + 1,
            "type": data.get("type"),
            "category": data.get("category"),
            "amount": float(data.get("amount")),
            "description": data.get("description"),
        }
        finance_data.append(new_transaction)
        return jsonify({"message": "Transaction added!", "transaction": new_transaction}), 201

    # Just return transactions as before
    return jsonify(finance_data), 200

@app.route('/transactions/api/<int:transaction_id>', methods=['GET', 'PUT', 'DELETE'])
def transaction_detail(transaction_id):
    """Handle retrieving, updating, or deleting a single transaction."""
    transaction = next((t for t in finance_data if t["id"] == transaction_id), None)
    if not transaction:
        return jsonify({"error": "Transaction not found"}), 404

    if request.method == 'GET':
        return jsonify(transaction), 200

    elif request.method == 'PUT':
        # Update a transaction
        data = request.get_json()
        transaction.update({
            "type": data.get("type", transaction["type"]),
            "category": data.get("category", transaction["category"]),
            "amount": data.get("amount", transaction["amount"]),
            "description": data.get("description", transaction["description"]),
        })
        return jsonify({"message": "Transaction updated!", "transaction": transaction}), 200

    elif request.method == 'DELETE':
        # Delete a transaction
        finance_data.remove(transaction)
        return jsonify({"message": "Transaction deleted!"}), 200

@app.route('/add_transaction')
def add_transaction():
    """Render the add transaction page."""
    return render_template('add_transaction.html')


if __name__ == "__main__":
    app.run(debug=True)
