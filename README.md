# PYMR
Pymr is a small python wrapper for map-reduce programming in hadoop streaming mode. It imitates many operations as Java MR framework. One can simply override map() or reduce() method to make code running in streaming mode.  
https://github.com/kn45/PyMR

## Features
Never bother with input, group by key, which have been handled by Pymr. Just override such method:  

- Mapper:  
_setup(self), _map(self, inl), _cleanup(self)
- Reducer:  
_setup(self), _reduce(self, key, values), _cleanup(self)  
self.delim, self.key_fields

## Example
`cat test_in | python test.py m | sort | python test.py r`

## Todo
Lots. Add more functions such as counter, env_getter etc.
