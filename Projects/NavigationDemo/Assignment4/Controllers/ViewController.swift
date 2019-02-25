//
//  ViewController.swift
//  NavigationDemo
//
//  Created by tanaka on 2/19/19.
//  Copyright © 2019 tanaka. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var labelNumber: UILabel!
    
    var numberValue: String?
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    override func viewWillAppear(_ animated: Bool) {
        if let numberValue = numberValue {
            labelNumber.text = numberValue
        }
            
    }

    @IBAction func saveButtonTouched(_ sender: UIBarButtonItem) {
        
        //code tosave or add new
        // navigate bage
        
        self.navigationController?.popViewController(animated: true)
    }
    
}

