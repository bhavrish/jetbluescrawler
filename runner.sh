#! /bin/bash

airlines=( jetblue american united spirit )
categories=( Available BaggageFees Connections Cost FamilyOptions FoodEntertainment HiddenFees Legroom Reimbursement Service Time TravelRewards )

for airline in "${airlines[@]}"
do
    for category in "${categories[@]}"
    do
	python3 manage.py "${airline}${category}"
    done
done

