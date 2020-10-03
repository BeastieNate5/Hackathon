using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class touch : MonoBehaviour
{
    public GameObject player;
    void OnCollisionEnter()
    {
        StartCoroutine(wait());
        
    }
    IEnumerator wait()
    {
        
        yield return new WaitForSeconds(0.1f);
        player.transform.position = new Vector3(0, 2f, 0);

    }

}
