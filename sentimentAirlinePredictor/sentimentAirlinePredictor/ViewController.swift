//
//  ViewController.swift
//  sentimentAirlinePredictor
//
//  Created by Bhavesh Shah on 10/26/19.
//  Copyright © 2019 Bhavesh Shah. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    let model = SentimentDetector()
    @IBOutlet weak var tweetField: UITextField!
    @IBOutlet weak var classificationLabel: UILabel!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func onSubmit(_ sender: Any) {
        let tweet=tweetField.text
        let retweet=0
        guard let sentimentOutput = try? model.prediction(text:tweet!) else {
            fatalError("Unexpected runtime error.")
        }
        classificationLabel.text=sentimentOutput.label
    }
    
}

