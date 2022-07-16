def zap_get_alerts(zap, baseurl, denylist, out_of_scope_dict):
    st = 0
    pg = 5000    false_positives = [(10096, 'http://example.com')]
    alerts = zap.core.alerts(baseurl=baseurl, start=st, count=pg)
    while len(alerts) > 0:
        for alert in alerts:
          alert_id = alert.get('id')
          url = alert.get('url')
          plugin_id = alert.get('pluginId')
            
            for fp in false_positives:
              if plugin_id == fp[0] and url == fp[1]:
                zap.alert.update_alerts_confidence(alert_id, '0')
         st += pg
         alerts = zap.core.alerts(start=st, count=pg)
    return alerts
