ckan.module('apihelper', function (jQuery, _) {
  return {
    initialize: function () {
      this.el.change(this.change);
    },
    change: function (e) {
      var helparea = $('#apihelper-help');
      var help_text = "Select an endpoint to see it's documentation.";
      // get element only if it exists
      if(action_help[e.val] !== undefined) {
        help_text = action_help[e.val];
      }
      // get the newlines converted properly
      help_text = help_text.replace(/\n/g, '<br />')
      helparea.html(help_text);
    },
  };
});
ckan.module('apihelper-submit', function (jQuery, _) {
  return {
    initialize: function () {
      $.proxyAll(this, /_on/);
      this.el.click(this._onClick);
    },
    _onClick: function (e) {
      e.preventDefault();
      var action = $('#field-actions option:selected')[0].value;
      var output = '';
      if(action_help[action] === undefined) {
        return
      }
      if (this.options.action === 'get') {
        this._getAction(action);
      } else {
        this._postAction(action);
      }
    },
    _getAction: function (action) {
      var next = false;
      var param_count = 0;
      var param_key_sel = '';
      var param_val_sel = '';
      var param_key = '';
      var param_val = '';
      var param_string = '?'
      do {
        param_key_sel = '#field-extras-' + param_count + '-key';
        param_val_sel = '#field-extras-' + param_count + '-value';
        param_key = $(param_key_sel).val();
        param_val = $(param_val_sel).val();
        if (param_key === undefined || param_val === undefined) {
          next = false;
          break;
        }
        if (param_key !== '' && param_val !== '') {
          param_string += param_key + '=' + param_val + '&';
        }
        param_count++
      } while (next === true);
      var r = $.get(ckan.SITE_ROOT + '/api/3/action/' + action + param_string, function(data) {
        var output_area = $('#apihelper-output');
        output_area.removeClass('invisible');
        output_area.text(JSON.stringify(data, null, "    "));
      });
      r.fail(function(data) {
        console.log('failed with %o', data);
      });
    },
    _postAction: function (action) {
      var postData = $('#apihelper-data').val();
      var r = $.post(ckan.SITE_ROOT + '/api/3/action/' + action, postData, function(data) {
        console.log(data)
        var output_area = $('#apihelper-output');
        output_area.removeClass('invisible');
        output_area.text(JSON.stringify(data, null, "    "));
      });
      r.fail(function(data) {
        console.log('failed with %o', data);
        var output_area = $('#apihelper-output');
        output_area.removeClass('invisible');
        output_area.text(JSON.stringify(data, null, "    "));
      });
    },
  };
});
