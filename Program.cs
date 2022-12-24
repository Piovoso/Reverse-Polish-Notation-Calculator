using System;
using System.Data;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace calc
{
    public class Calculator
    {
        List<string> RPNOperator = new(){}; // First In First Out (FIFO)
        List<string> RPNOutput = new(){};   // Last In First Out  (LIFO)
        public double? Value { get; set; }  // Equation Value
        public static void Main()
        {
            Console.WriteLine($"Mathematical Operators:\n^ :Power | * :Multiply | / :Divide | + :Plus | - :Minus\nExample: 10^2-3+4503/2\n");
            var expression = Console.ReadLine(); // Equation Expression

            var calculator = new Calculator();

            foreach (var chr in expression) {
                calculator.KeyPress(chr);
            }

            while (true)
            {
                if (calculator.RPNOperator.Contains("^"))
                {
                    int indexOfOperator = calculator.RPNOperator.IndexOf("^");
                    
                    double MathematicalExpression = Math.Pow(double.Parse(calculator.RPNOutput.ElementAt(indexOfOperator)), double.Parse(calculator.RPNOutput.ElementAt(indexOfOperator + 1)));
                    calculator.Removal(MathematicalExpression, indexOfOperator);
                }
                else if (calculator.RPNOperator.Contains("*") || calculator.RPNOperator.Contains("/")) //Checks if the Operator stack contains Multiplication (*) or Division (/)
                {   //Checks if it contains multiplication (*) and if it is higher than division (/)
                    if (calculator.RPNOperator.Contains("*") && calculator.RPNOperator.IndexOf("*") < 1)
                    {
                        int indexOfOperator = calculator.RPNOperator.IndexOf("*"); // Indexes the Operator for reference, Probably could be done in the line itself
                        // Does the Math by converting to Double (* : operator)
                        double MathematicalExpression = double.Parse(calculator.RPNOutput.ElementAt(indexOfOperator)) * double.Parse(calculator.RPNOutput.ElementAt(indexOfOperator + 1));
                        calculator.Removal(MathematicalExpression, indexOfOperator); // Removes unnessecary Items from the list and inserts the new value into the list (Lines 84-91)
                    }
                    else // If it doesn't contain Multiplication (*) or if the index of Multiplication (*) is not higher than division (/) it runs this
                    { 
                        int indexOfOperator = calculator.RPNOperator.IndexOf("/");
                        // Does the Math by converting to Double (/ : operator)
                        double MathematicalExpression = double.Parse(calculator.RPNOutput.ElementAt(indexOfOperator)) / double.Parse(calculator.RPNOutput.ElementAt(indexOfOperator + 1));
                        calculator.Removal(MathematicalExpression, indexOfOperator);
                    }
                } // Equal Status Operators.
                else if (calculator.RPNOperator.Contains("+") || calculator.RPNOperator.Contains("-")) //Checks if the Operator stack contains Addition (+) or Subtraction (-) Due
                {
                    if (calculator.RPNOperator.Contains("+") && calculator.RPNOperator.IndexOf("+") < 1)
                    {
                        int indexOfOperator = calculator.RPNOperator.IndexOf("+");
                        // Does the Math by converting to Double (+ : operator)
                        double MathematicalExpression = double.Parse(calculator.RPNOutput.ElementAt(indexOfOperator)) + double.Parse(calculator.RPNOutput.ElementAt(indexOfOperator + 1));
                        calculator.Removal(MathematicalExpression, indexOfOperator); 
                    }
                    else
                    {
                        int indexOfOperator = calculator.RPNOperator.IndexOf("-");
                        // Does the Math by converting to Double (- : operator)
                        double MathematicalExpression = double.Parse(calculator.RPNOutput.ElementAt(indexOfOperator)) - double.Parse(calculator.RPNOutput.ElementAt(indexOfOperator + 1));
                        calculator.Removal(MathematicalExpression, indexOfOperator);
                    }
                } else { Console.WriteLine($"Incorrect Operator: {calculator.RPNOperator.First()}"); break; }

                if (calculator.RPNOutput.Count == 1) // If the length of the list is equal to 1 then it Gives calculator.Value a value from the list.
                { // If it doesn't get here, it's broken and given a non calculatable value.
                    calculator.Value = double.Parse(calculator.RPNOutput.FirstOrDefault()); break; //Converts to Double since the element in the list is a string.
                }
            }

            Console.WriteLine($"\nAnswer: {calculator.Value}");
        }
        public void KeyPress(char key)
        {
            string digit = key.ToString();
            if (digit == " ") { return; } // test if item is Space, skips If it is.

            if (key.ToString().All(char.IsDigit)) // Digit Stack (LIFO)
            {
                if (RPNOutput.Count > RPNOperator.Count)    // Test if number is greater than 1 character
                {
                    string digitAdd = RPNOutput.Last();     // Retrives the last (string)digit added
                    RPNOutput.RemoveAt(RPNOutput.Count - 1);// Combines them to one number
                    digit = digitAdd + digit;
                }
                RPNOutput.Add(digit);   // Pushes into stack

            } else {                    // Operator Queue (FIFO)
                RPNOperator.Add(digit); // Queues the new operator.
            }
        }
        public void Removal(double mathematic,
                            int indexof)
        {
            RPNOutput.RemoveAt(indexof);    // removes the index of the matematical operator, since the operator is at the same index as the values needed to math with.
            RPNOutput.RemoveAt(indexof);    // removes it twice, since the other value is moved down by one.
            RPNOperator.RemoveAt(indexof);  // removes the operator so it doesn't do it twice

            RPNOutput.Insert(indexof,       // Puts the Value back into the position it is supposed to be in, same index as the operator was.
                             mathematic.ToString());
        }
    }
}