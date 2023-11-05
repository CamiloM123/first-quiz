package org.velezreyes.quiz.question6;

/**
 * Class representing a drink.
 * This class represents a beverage with a name and a property to indicate if it's fizzy.
 * 
 * @version 1.0.0
 * @author Camilo Muñoz
 */
public interface Drink {
  
  /**
   * Getter for the name property.
   * 
   * @return The name of the drink.
   */
  public String getName();
  
  /**
   * Getter for the isFizzy property.
   * 
   * @return A boolean indicating if the drink is fizzy.
   */
  public boolean isFizzy();
}