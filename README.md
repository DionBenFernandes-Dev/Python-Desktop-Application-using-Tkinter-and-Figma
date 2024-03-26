# Python-Desktop-Application-using-Tkinter-and-Figma
The Budget Tracker, built with Python and Tkinter, offers a user-friendly interface for monitoring income, expenses, and balance. It leverages Figma for design collaboration, showcasing effective financial management in a compact application.

The Budget Tracker project is a comprehensive solution aimed at assisting users in managing their financial resources effectively. Developed using Python and Tkinter for the frontend, and leveraging fundamental concepts of GUI programming, the application offers an intuitive interface for users to monitor their income, expenses, and overall balance.

At its core, the application utilizes Tkinter for creating a visually appealing and interactive user interface. Tkinter provides various widgets such as buttons, text entries, and canvas elements, facilitating the construction of a responsive and dynamic layout.

The project integrates essential functionalities such as inputting expenses, calculating balances, and displaying the financial data in real-time. Users can conveniently add their expenses, triggering automatic updates to the overall balance displayed on the interface.

Moreover, the project demonstrates proficiency in handling data and performing calculations within the Python environment. By incorporating global variables and event-driven programming, the application ensures seamless interaction between different components.

In addition to technical implementation, the project emphasizes the importance of design in software development. Figma, a collaborative interface design tool, plays a pivotal role in conceptualizing and prototyping the application's user interface. By utilizing Figma, designers and developers collaborate effectively to create a visually appealing and user-friendly layout.

Overall, the Budget Tracker project not only showcases technical skills in Python programming and GUI development but also underscores the significance of user-centered design principles in delivering a compelling software solution for financial management.

Here are the steps to create a virtual environment (assuming you have Python installed on your system):

1. **Open Terminal/Command Prompt:**
   Open your terminal or command prompt application. You can find this in your system's applications or by searching for "Terminal" (on macOS/Linux) or "Command Prompt" (on Windows).

2. **Navigate to your Project Directory:**
   Use the `cd` command to navigate to your project directory. For example:
   ```
   cd path/to/Budget-Tracker
   ```

3. **Install Virtualenv (if not already installed):**
   If you haven't installed `virtualenv` yet, you can do so via pip, Python's package installer:
   ```
   pip install virtualenv
   ```

4. **Create the Virtual Environment:**
   Once `virtualenv` is installed, you can create a virtual environment using the following command:
   ```
   python -m venv .venv
   ```
   This command creates a virtual environment named `.venv` in your project directory.

5. **Activate the Virtual Environment:**
   After the virtual environment is created, you need to activate it. The activation command varies depending on your operating system:
   - **On macOS/Linux:**
     ```
     source .venv/bin/activate
     ```
   - **On Windows:**
     ```
     .venv\Scripts\activate
     ```

6. **Verify Activation:**
   Once activated, you'll notice that the command prompt changes to indicate the activated virtual environment. Additionally, you can use the `which python` command (on macOS/Linux) or `where python` command (on Windows) to verify that the Python interpreter used is now from the virtual environment.

Now, your virtual environment is set up and activated. You can install dependencies, run your Python scripts, and manage your project without affecting system-wide Python installations. When you're done working on your project, you can deactivate the virtual environment using the `deactivate` command.

Here's a step-by-step guide on how to use the code from GitHub, assuming you've already set up your virtual environment:

1. **Clone the Repository:**
   ```
   git clone <repository_url>
   ```

2. **Navigate to the Budget-Tracker Directory:**
   ```
   cd Budget-Tracker
   ```

3. **Create/Activate the Virtual Environment:**
   ```
   source .venv/bin/activate
   ```

5. **Run the Application:**
   ```
   python build/gui.py
   ```
   This command will execute the `gui.py` file located in the `build` folder.

6. **Interact with the Application:**
   Once the application window opens, you can start using the budget tracker. Input your expenses in the designated field and click the submit button to update the displayed expenses and balance.

9. **Deactivate Virtual Environment:**
   Once you're done using the application, deactivate the virtual environment:
   ```
   deactivate
   ```

By following these steps, you can effectively utilize the Budget Tracker application from GitHub, collaborate on design using Figma, and manage your project within a virtual environment for a clean and isolated development environment.

![Project Image](https://github.com/DionBenFernandes-Dev/Python-Desktop-Application-using-Tkinter-and-Figma/blob/main/Screenshot%202024-03-26%20120947.png)
