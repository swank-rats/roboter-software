roboter-software
================

Software for Rat-Roboter


Actual protocol:

```javascript
{
    to: 'test',
    cmd: 'echo',
    params: {
        toUpper: true
    },
    data: 'testdata'
}
```

Implementet functionallity:

```javascript
{
    to: 'robot',
    cmd: 'left'
}

{
    to: 'robot',
    cmd: 'right'
}

{
    to: 'robot',
    cmd: 'straight'
}

{
    to: 'print',
}
```
