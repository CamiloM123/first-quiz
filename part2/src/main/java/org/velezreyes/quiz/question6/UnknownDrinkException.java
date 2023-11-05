package org.velezreyes.quiz.question6;

/**
 * Exception thrown when the user tries to buy a drink that is not available.
 * 
 * @version 1.0.0
 * @see VendingMachineImpl
 */
public class UnknownDrinkException extends Exception {

  /**
   * Constructor for the NotEnoughMoneyException class.
   */
  public UnknownDrinkException(String name) {
    super("Unknown drink: " + name);
  }
}
