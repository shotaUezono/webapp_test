var url = window.location.search

        var val = getUrlVars();

        /**
        * URL analyze and Return query
        * @returns {Array} query string
        */

        function getUrlVars(){
            var vars = [];
            var max = 0;
            var hash = "";
            var array = "";

            hash = url.slice(1).split('&');
            max = hash.length;
            for(var i = 0; i < max; i++){
                array = hash[i].split("=");
                vars[array[0]] = array[1];
            }
            return vars;
        }

        console.log(val);
        var user = val["user"];
        document.getElementsByName("username").value = user;
