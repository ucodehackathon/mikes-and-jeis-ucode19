(function () {
    'use strict';

    var app = angular.module("myApp", []);



    app.controller("myCtrl", ['$scope', '$http','$rootScope', function ($scope, $http,$rootScope) {
        $rootScope.nameFile="Drop Here";
        $scope.changeName = function () {
            $scope.nameFile = document.getElementById('inputGroupFile04').files[0].name;
        };
        $scope.add = function () {
            var f = document.getElementById('inputGroupFile04').files[0],
                r = new FileReader();

            console.log(f);

            r.onloadend = function (e) {
                var data = e.target.result;
                //send your binary data via $http or $resource or do anything else with it

                $http({
                    method: 'POST',
                    url: '/find',
                    headers: {
                        'Content-Type': "application/csv"
                    },
                    data: {
                        file: data,
                        name: f.name
                    }
                }).then(function successCallback(response) {
                    console.log(response.data)
                    alert(response.data);
                }, function errorCallback(response) {
                    console.log("mal");
                });
                console.log(f.name);
                console.log(e);
            }


            r.readAsBinaryString(f);
        }


    }]);



}
());