import streamlit as st

# Define the ATM class using OOP concepts
class SimpleATM:
    def __init__(self, initial_balance=0):
        # Initialize the balance as an instance variable
        self.balance = initial_balance

    def check_balance(self):
        # Method to return the current balance
        return self.balance

    def deposit(self, amount):
        # Method to handle deposits
        if amount > 0:
            self.balance += amount
            return f"Successfully deposited ₹{amount:.2f}. New balance: ₹{self.balance:.2f}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        # Method to handle withdrawals
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Successfully withdrew ₹{amount:.2f}. Remaining balance: ₹{self.balance:.2f}"
            else:
                return "Insufficient funds. Withdrawal denied."
        else:
            return "Withdrawal amount must be positive."

# --- Streamlit User Interface ---

st.title("Simple ATM Application (No Database)")

# Use Streamlit's session state to persist the ATM object
# This keeps the balance across user interactions without a database
if 'atm' not in st.session_state:
    st.session_state.atm = SimpleATM(initial_balance=1000) # Start with an initial balance

# Get the ATM object from session state
current_atm = st.session_state.atm

# Display current balance
st.subheader("Account Balance")
st.info(f"Your current balance is: ₹{current_atm.check_balance():.2f}")

st.markdown("---")

# Deposit section
st.subheader("Make a Deposit")
deposit_amount = st.number_input("Enter amount to deposit:", min_value=0.01, format="%.2f")
if st.button("Deposit Funds"):
    message = current_atm.deposit(deposit_amount)
    st.success(message)
    st.rerun() # Rerun the app to update the displayed balance

st.markdown("---")

# Withdraw section
st.subheader("Make a Withdrawal")
withdraw_amount = st.number_input("Enter amount to withdraw:", min_value=0.01, format="%.2f")
if st.button("Withdraw Funds"):
    message = current_atm.withdraw(withdraw_amount)
    if "Insufficient funds" in message:
        st.error(message)
    else:
        st.success(message)
    st.rerun() # Rerun the app to update the displayed balance
