//
//  jetBlueClassifier.swift
//
//
//  Created by Bhavesh Shah on 10/26/19.
//

import CreateML
import Foundation
//1
let data = try MLDataTable(contentsOf: URL(fileURLWithPath: "/Users/bhaveshshah/Downloads/csvjson.json"))
let (trainingData, testingData) = data.randomSplit(by: 0.8, seed: 5)
let sentimentClassifier = try MLTextClassifier(trainingData: trainingData, textColumn: "text", labelColumn: "airline_sentiment")
//2
let trainingAccuracy = (1.0 - sentimentClassifier.trainingMetrics.classificationError) * 100
let validationAccuracy = (1.0 - sentimentClassifier.validationMetrics.classificationError) * 100
//3
let evaluationMetrics = sentimentClassifier.evaluation(on: testingData)
let evaluationAccuracy = (1.0 - evaluationMetrics.classificationError) * 100
//4
let metadata = MLModelMetadata(author: "Bhavesh Shah", shortDescription: "A model trained to classify Jet Blue flight reviews based on Tweets", version: "1.0")
try sentimentClassifier.write(to: URL(fileURLWithPath: "/Users/bhaveshshah/Desktop/jetblue/SentimentDetector.mlmodel"), metadata: metadata)
