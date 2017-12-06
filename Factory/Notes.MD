# Factory Method

**Goals:**
1. Allow child classes to take care of the instantiation for multiple cases. 
2. Uses methods to deal with creating objects without having to specify class of the object
3. Object creation is handled by the subclasses by passing it through methods on the factory 


**Example:**

Consider a group of Shapes. These shapes include Circle and Rectangle. If we need to find out the center of the Circle or height of Rectangle, we can do this without 
explicity having to create these classes

