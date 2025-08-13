
# Python Data Science Snippets

A comprehensive collection of simple, reusable code snippets for NumPy, Pandas, Matplotlib, and Seaborn. Perfect for quick reference, learning, and accelerating your data science workflow.

## 🎯 Overview

This repository contains practical, well-documented code snippets that demonstrate common operations and techniques in Python data science. Each snippet is designed to be self-contained, well-commented, and beginner-friendly while being practical for real-world data science tasks.

Whether you're a beginner learning the basics or an experienced developer looking for quick references, these snippets will help you work more efficiently with data in Python.

## 🛠 Libraries Overview

### NumPy
**Numerical Python** - The fundamental package for scientific computing in Python.

NumPy provides powerful N-dimensional array objects and a collection of mathematical functions to operate on these arrays. It's the foundation of the Python data science ecosystem, offering:
- High-performance multidimensional array objects (ndarray)
- Mathematical functions for arrays (trigonometric, logarithmic, statistical)
- Tools for array manipulation, reshaping, and indexing
- Linear algebra operations and random number generation
- Broadcasting capabilities for efficient computation

**Key Use Cases**: Scientific computing, mathematical operations, array processing, serving as the base for other data science libraries.

### Pandas
**Python Data Analysis Library** - Powerful data structures and data analysis tools.

Pandas provides high-level data structures (DataFrame and Series) and data analysis tools that make data manipulation and analysis easy and intuitive. It's built on top of NumPy and offers:
- DataFrame and Series objects for structured data
- Data cleaning and preparation tools
- Reading/writing data from various formats (CSV, Excel, JSON, SQL, etc.)
- Data grouping, merging, and reshaping operations
- Time series analysis and handling missing data
- Powerful indexing and selection capabilities

**Key Use Cases**: Data cleaning, data transformation, exploratory data analysis, handling structured data, data preprocessing for machine learning.

### Matplotlib
**Python 2D Plotting Library** - Comprehensive library for creating static, animated, and interactive visualizations.

Matplotlib is the most widely used plotting library in Python, providing a MATLAB-like interface for creating high-quality plots and charts. It offers:
- Wide variety of plot types (line, scatter, bar, histogram, pie, etc.)
- Fine-grained control over plot appearance and styling
- Support for subplots and complex figure layouts
- Extensive customization options for colors, fonts, and annotations
- Export capabilities to various formats (PNG, PDF, SVG, etc.)
- Integration with Jupyter notebooks and GUI applications

**Key Use Cases**: Data visualization, scientific plotting, creating publication-quality figures, exploratory data analysis visualizations.

### Seaborn
**Statistical Data Visualization** - High-level interface for drawing attractive and informative statistical graphics.

Seaborn is built on top of Matplotlib and provides a higher-level interface for creating beautiful statistical visualizations. It's designed to work seamlessly with Pandas DataFrames and offers:
- Built-in themes and color palettes for attractive plots
- Statistical plotting functions (regression plots, distribution plots)
- Easy visualization of relationships in datasets
- Automatic handling of categorical data
- Advanced plot types like heatmaps, pair plots, and facet grids
- Integration with statistical analysis workflows

**Key Use Cases**: Statistical data visualization, exploring relationships between variables, creating publication-ready statistical plots, data exploration and presentation.

---

**Happy coding! 🐍📊**ematical Functions**: Trigonometric, logarithmic, statistical
- **Array Manipulation**: Reshaping, concatenation, splitting
- **Linear Algebra**: Matrix multiplication, eigenvalues, decomposition
- **Random Number Generation**: Various distributions and sampling

### Pandas Snippets
- **Data Loading**: Reading from CSV, Excel, JSON, databases
- **Data Exploration**: Head, tail, info, describe, value counts
- **Data Cleaning**: Handling missing values, duplicates, data types
- **Data Transformation**: Apply functions, string operations, datetime
- **Data Analysis**: Groupby, pivot tables, cross-tabulation

### Matplotlib Snippets
- **Basic Plots**: Line, scatter, bar, pie charts
- **Plot Customization**: Colors, markers, labels, titles
- **Subplots**: Multiple plots in one figure
- **Annotations**: Text, arrows, shapes
- **Export**: Saving plots in different formats (PNG, PDF, SVG)

### Seaborn Snippets
- **Distribution Plots**: Histograms, KDE, box plots, violin plots
- **Relationship Plots**: Scatter plots, line plots, regression plots
- **Categorical Plots**: Bar plots, count plots, point plots
- **Matrix Plots**: Heatmaps, cluster maps
- **Styling**: Themes, color palettes, context settings

## 💡 Usage Examples

### NumPy Example
```python
import numpy as np

# Create arrays and perform operations
arr = np.array([1, 2, 3, 4, 5])
result = np.sqrt(arr) * 2
print(f"Result: {result}")
```

### Pandas Example
```python
import pandas as pd

# Data manipulation
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = df['A'] + df['B']
grouped = df.groupby('A').sum()
```

### Visualization Example
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Create a beautiful plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='A', y='B', size='C')
plt.title('Scatter Plot with Size Mapping')
plt.show()
```

## 📖 Resources

### Official Documentation
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [Seaborn Documentation](https://seaborn.pydata.org/)

### Learning Resources
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)

### Datasets for Practice
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/)
- [Seaborn Built-in Datasets](https://github.com/mwaskom/seaborn-data)

## 🏷 Tags

`python` `data-science` `numpy` `pandas` `matplotlib` `seaborn` `snippets` `examples` `tutorial` `reference`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⭐ Show Your Support

If you find this repository helpful, please give it a star! It helps others discover these resources.

---

**Happy coding! 🐍📊**

> "In data science, the journey of a thousand insights begins with a single snippet."
