(function() {
    var cubes, list, math, num, number, opposite, race, square,
        __slice = Array.prototype.slice;
    number = 42;

    opposite = true;
//TODO comment code
    if (opposite) number = -42;

    square = function(x) {
        return x * x;
    };

    list = [1, 2, 3, 4, 5];

    //TODO-bob region Description
    math = {
        root: Math.sqrt,
        square: square,
        cube: function(x) {
            return x * square(x);
        }
    };
    race = function() {
        var runners, winner;
//    todo-me have a break

        //endregion
//TODO-john fix
        winner = arguments[0], runners = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
        return print(winner, runners);
    };
    if (typeof elvis !== "undefined" && elvis !== null ? elvis : cubes = (function() {
        var _i, _len, _results;
        _results = [];
        for (_i = 0, _len = list.length; _i < _len; _i++) {
            num = list[_i];
            _results.push(math.cube(num));
        }
        return _results;
    })()) {
        alert("I knew it");
    }

}).call(this);

