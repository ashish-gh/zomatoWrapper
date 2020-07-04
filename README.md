# zomatoWrapper

Zomato API integration with python

![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

# Quick start


```bash
$ pip install zomatoWrapper
```
or

```bash
$ python setup.py install
```

# Authentication

Register for an API key:

All you need to do is [register](https://developers.zomato.com/api) in order to get your API key, a mandatory parameter for most of our API calls. It’s your personal identifier and should be kept secret.

# Usage

With your key in hand, it's time to authenticate, so run:

```python
>>> from zomatoWrapper import Zomato

>>> zomato = Zomato('<apikey>')
```

## Categories Get

This api provides you the list of categories.

Parameters:

Returns: categories ''dict''
- categoryId - ID of the category type.
- categoryName - Name of the category type.
```python
>>> zomato.getCategories()
```
## CityId Get

This api provides you name.

Parameters: cityName : ''str''
- cityName - Name of city i.e. Los Angles.
     
Returns: cityId ''int''
- cityId - unique id for city.
```python
>>> zomato.getCityID(123)
```
