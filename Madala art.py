import turtle
# Function for floral design or mandala art
def draw_floral_design(color, pattern):
    turtle.speed(10)
    turtle.color(color)
    for _ in range(36):
        for _ in range(5):
            turtle.forward(100)
            turtle.right(90)
        turtle.right(10)
    turtle.done()

# different floral designs or mandala art with colors and patterns
mandala_designs = [
    {"color": "red", "pattern": "flower"},
    {"color": "blue", "pattern": "star"},
    {"color": "green", "pattern": "circle"},
    {"color": "purple", "pattern": "triangle"},
    {"color": "orange", "pattern": "square"}]


def select_design(design_number):
    design = mandala_designs[design_number - 1]
    draw_floral_design(design["color"], design["pattern"])

# user input to select the design
design_number = int(input("Enter the design number (1-5): "))
select_design(design_number)