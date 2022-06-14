var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";


MongoClient.connect(url, function (err, db) {
    if (err) throw err;
    var dbo = db.db("store");

    // Answer to the question no 1
    dbo.createCollection("Filling", function (err, res) {
        if (err) throw err;
        var rows = [
            { fillingID: 1, fillingName: '200g of tuna', fillingPrice: 1.01, fillingCalories: 0.37, menuItemId: 1, fillngCategory: 'fish' },
            { fillingID: 2, fillingName: '150g of tomato', fillingPrice: 0.41, fillingCalories: 0.25, menuItemId: 1, fillngCategory: 'vegetable' },
            { fillingID: 3, fillingName: '100g of cucumber', fillingPrice: 0.35, fillingCalories: 0.1, menuItemId: 1, fillngCategory: 'vegetable' },
            { fillingID: 4, fillingName: '100g of lettuce', fillingPrice: 0.23, fillingCalories: 0.21, menuItemId: 1, fillngCategory: 'vegetable' },
            { fillingID: 5, fillingName: '150g of gherkin', fillingPrice: 0.17, fillingCalories: 0.18, menuItemId: 1, fillngCategory: 'vegetable' },
            { fillingID: 6, fillingName: '50g of chicken', fillingPrice: 0.57, fillingCalories: 0.75, menuItemId: 2, fillngCategory: 'meat' }
        ]
        dbo.collection("Filling").insertMany(rows, function(err, res) {
            if (err) throw err;
            console.log("Number of documents inserted: " + res.insertedCount);

            // Answer to the question no 2
            dbo.collection("Filling").find({fillingName: {$regex: "s$"}}).toArray(function(err, result) {
                if (err) throw err;
                console.log(result);
                db.close();
              });
        });
    });
});