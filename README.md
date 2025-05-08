# "LOW" - Lowballer Optimal Workflow

**LOW** is a PyQt5-based desktop application designed to help users quickly generate customizable lowballing messages for Hypixel Skyblock. The application provides a user-friendly interface to input values, select rules, and generate formatted messages to bypass the spam filter on Hypixel.

---

## Features

- **Customizable Inputs**: Users can input their purse value and minimum item value, with default values of `200m` and `25m` respectively if no input is provided.
- **Rule Selection**: Select from predefined rules (e.g., "No Attributes", "No Dyes") to tailor your lowball messages.
- **Dynamic Message Generation**: Generates up to 5 unique messages at a time, with or without rules.
- **Copy Functionality**: Copy any generated message to the clipboard with a single click.
- **Responsive Design**: Modern, gradient-based UI with a clean and professional look.

---

## How It Works

### Input Page

1. **Purse and Minimum Input Fields**  
   - Enter your purse value and minimum item value.  
   - Leave fields blank to use default values (`200m` for purse, `25m` for minimum).

2. **Rule Selection**  
   - Choose from a set of rule checkboxes (e.g., "No Attributes", "No Dyes").  
   - If no rules are selected, simpler messages are generated.

3. **Buttons**  
   - **Generate Messages**: Generates up to 5 unique messages based on input and selected rules.  
   - **Quit**: Exits the application.

### Result Page

1. **Generated Messages**  
   - Displays up to 5 messages in a scrollable view, formatted based on your input and selected rules.

2. **Copy Button**  
   - Each message has a dedicated button to copy it to the clipboard.

3. **Navigation**  
   - **Back**: Return to the input page.  
   - **More**: Generate a new batch of messages.

---

## Message Templates

### With Rules

If rules are selected, messages include a formatted list of rules:

- `LOWBALLING {purse} | Min: {min} | {rules} | VISIT ME`
- `LOWBALLING {purse} → Min Value: {min} → No: {rules} → Come now!`

### Without Rules

Simpler templates are used:

- `LOWBALLING {purse} | Min: {min} | VISIT ME`
- `LOWBALLING {purse} → Min Value: {min} → Come now!`

### Extras

Each message may include a random suffix for variety:

- `""`, `"!!!"`, `" pls hurry"`, `" <3"`

---

## Code Overview

### Key Components

- **`LowballGenerator` Class**:  
  Main window class handling layout, state, and message generation.

- **`init_input_page` Method**:  
  Sets up the initial input UI with fields, rule checkboxes, and control buttons.

- **`init_result_page` Method**:  
  Displays results in a scrollable format with navigation and copy buttons.

- **`generate_messages` Method**:  
  Core logic that builds messages from inputs and rules.

- **`parse_amount` Method**:  
  Converts user-entered values like `200m` or `25k` into numerical values.

---

## Usage

1. Launch the application.
2. Input your purse and minimum item values (optional).
3. Select any relevant rules.
4. Click "Generate Messages" to produce up to 5 unique messages.
5. Copy messages as needed or generate a new batch.

---

## Styling

The app uses a custom QSS stylesheet for a modern UI:

- **Gradient Background**: Applied to the main window.
- **Custom Fonts**: All text uses Consolas.
- **Hover Effects**: Buttons change color when hovered.

---

## Contributing

Contributions are welcome!  
Feel free to submit issues or pull requests to help improve the application.

---

## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.
