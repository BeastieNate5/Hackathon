using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class danger : MonoBehaviour
{
    private MeshRenderer mr;
    public Material pass;
    public Material solid;
    private BoxCollider bc;


    bool canRun = true;
    // Start is called before the first frame update
    void Start()
    {
        bc = GetComponent<BoxCollider>();
        mr = GetComponent<MeshRenderer>();
    }

    // Update is called once per frame
    void Update()
    {
        if (canRun == true)
        {
            StartCoroutine(change());
        }
       
    }

    IEnumerator change()
    {
        canRun = false;
        bc.isTrigger = false;
        mr.material = solid;
        gameObject.layer = 8;
        yield return new WaitForSeconds(2f);
        bc.isTrigger = true;
        mr.material = pass;
        gameObject.layer = 0;
        yield return new WaitForSeconds(2f);
        canRun = true;

    }
}
