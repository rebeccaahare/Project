from flask import Flask, render_template, request

app = Flask(__name__)

# Define the search function
def search_reports(query):
    print("search_reports function called with query:", query)
    # Add your search logic here, for example:
    reports = [
        #Operations Puzzle Piece
        {"title": "Adjustments", "description": "This report shows the number of order and receipt adjustments.", "link": ""},
        {"title": "Batch Release Logging", "description": "This report shows information on batching such as orders in a batch, percentage of orders batched, average items and quantity in a batch.", "link": ""},
        {"title": "Company Groups", "description": "This report shows the company group name for each customer in SWIMS along with their warehouse, id, and if they are active.", "link": ""},
        {"title": "Cold Supplies", "description": "This report tracks how many cooler boxes and eco liners we are using by week in the warehouses", "link": ""},
        {"title": "Current Inventory", "description": "This report shows the current inventory quantity by SKU and customer in each warehouse.  It also shows the SKU case pack and cases per pallet.", "link": ""},
        {"title": "Customer Support Associate Activity", "description": "This report shows warehouse activity by customer support associate or CSA.  Warehouse activity includes orders and receipts.", "link": ""},
        {"title": "On Time Shipping - 2021", "description": "This report is for the on time shipping KPI for 2021.  It shows the percentage of orders where the SLA was met by customer, warehouse and mode.", "link": ""},
        {"title": "On Time Shipping - 2022", "description": "This report is for the on time shipping KPI for 2022.  It shows the percentage of orders where the SLA was met by customer, warehouse and mode.", "link": ""},
        {"title": "On Time Shipping - 2023", "description": "This report is for the on time shipping KPI for 2023.  It shows the percentage of orders where the SLA was met by customer, warehouse and mode.", "link": ""},
        {"title": "Order Count by Shipping Destination", "description": "This report is in a map view and shows the order quantity by the ship to zip and state.", "link": ""},
        {"title": "Order Details", "description": "This report shows order details by customer such as count of orders with eaches, cases, and pallets, average lines, and average cubic feet.  This report also has a pareto chart that can show by customer the Total quantity shipped by SKU, current inventory, and current cubic feet.", "link": ""},
        {"title": "Order and Receipt Count", "description": "This report shows order and receipt count by customer, warehouse, mode, and method.", "link": ""},
        {"title": "LTH & FTE Trending", "description": "This report shows projected, targeted and the variance for LTH and FTE in the warehouses.", "link": ""},
        {"title": "Out of Scope Analysis", "description": "This report shows by warehouse and customer the count of out of scope or OOS entries along with the hours recorded in SWIMS.", "link": ""},
        {"title": "Order Shipping Method Changes", "description": "This report shows by warehouse and customer the count of shipping method changes at the ship station.", "link": ""},
        {"title": "Outbound Billing Rates", "description": "This report shows by customer the order and parcel rates.  It also shows the comparison of rates by customer.", "link": ""},
        {"title": "Parcel Package Count", "description": "This report shows the number of packages and orders by customer and warehouse.  It also shows the ratio of packages to orders.", "link": ""},
        {"title": "PHR Using SmartWorks & UltiPro", "description": "This report shows the customer and warehouse productive handling rate.  The handling revenue comes from NetSuite while the hours data comes from UltiPro and SmartWorks.  The hours are grossed up to each customer by the percentage of customer hours submitted in SWIMS.", "link": ""},
        {"title": "Shipping Method Analysis", "description": "This report shows order count by customer, method, and order type.  It also has a page that shows the shipping configuration in SWIMS for each customer.", "link": z""},
        {"title": "SKU Count by Company Group", "description": "This report shows the SKU count by company group name.", "link": ""},
        {"title": "SKU Validation", "description": "This report shows the SKU details by customer including if the SKU has been validated.", "link": ""},
        {"title": "Smoke Detector", "description": "This report was built for the smoke detectors with different metrics to track where something may be off.  This report uses data from mutliple other Power BI reports.", "link": ""},
        {"title": "SWIMS vs SmartWorks Labor Hours", "description": "This report compares the hours that are in SmartWorks versus the hours that are submitted in SWIMS by warehouse.", "link": ""},
        {"title": "Weekly Shipping Method Changes", "description": "This report shows by warehouse and customer how many times the shipping method changes at the ship station.", "link": ""},
        {"title": "WH Capacity", "description": "This report shows by warehouse and by customer what cubic feet is being used.  It shows current customers with their receipts coming, their dedicated storage, and customers who are in the sales pipeline", "link": ""},
        {"title": "WH Location Map", "description": "This report is a map visual that shows the different locations of all of the warehouses.", "link": ""}
    ]
    results = []
    for report in reports:
        if query in report["title"].lower() or query in report["description"].lower():
            results.append(report)
    return results

# Define the homepage route
@app.route("/")
def index():
    return render_template("index.html")

# Define the search results route
@app.route("/search")
def search():
    query = request.args.get("q", "")
    results = search_reports(query)
    return render_template("search.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=False, port=8001)
