package org.velezreyes.quiz.question6;

/**
 * Interface representing a vending machine.
 * This interface represents a vending machine that sells drinks.
 * 
 * @version 1.0.0
 * @author Camilo Muñoz
 */
public interface VendingMachine {

  /**
   * Inserts a quarter into the vending machine.
   * 
   */
  public void insertQuarter();

  /**
   * Chooses a drink from the vending machine.
   * @param name The name of the drink.
   * @throws NotEnoughMoneyException 
   * @throws UnknownDrinkException 
   */
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException;
}