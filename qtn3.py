#include <iostream>
#include <iomanip> // for setting decimal precision
using namespace std;

int main() {
    // Declare variables
    double balance, totalCost = 0, surcharge, vat;
    int waterUnits;
    const double VAT_RATE = 0.18, SURCHARGE_RATE = 0.15;
    
    // Prompt the user for the balance and the number of water units consumed
    cout << "Enter the amount of money loaded onto your account (UGX): ";
    cin >> balance;
    
    cout << "Enter the number of water units consumed: ";
    cin >> waterUnits;
    
    // Calculate the total cost based on the tiered pricing structure
    if (waterUnits <= 10) {
        totalCost = waterUnits * 150;
    } else if (waterUnits <= 20) {
        totalCost = (10 * 150) + ((waterUnits - 10) * 175);
    } else {
        totalCost = (10 * 150) + (10 * 175) + ((waterUnits - 20) * 200);
    }
    
    // Apply the 15% surcharge
    surcharge = totalCost * SURCHARGE_RATE;
    totalCost += surcharge;
    
    // Apply the 18% VAT
    vat = totalCost * VAT_RATE;
    totalCost += vat;
    
    // Check if the balance is sufficient
    if (balance >= totalCost) {
        balance -= totalCost;
        cout << fixed << setprecision(2); // To display amounts with 2 decimal places
        cout << "Transaction successful!" << endl;
        cout << "Total cost (including surcharge and VAT): " << totalCost << " UGX" << endl;
        cout << "Remaining balance: " << balance << " UGX" << endl;
    } else {
        cout << "Error: Insufficient balance." << endl;
        cout << "Your current balance: " << balance << " UGX" << endl;
        cout << "Total cost (including surcharge and VAT): " << totalCost << " UGX" << endl;
    }

    return 0;
}
