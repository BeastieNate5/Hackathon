using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class JumpPowerUp : MonoBehaviour
{
    public CubeSCR player;
    public Material powerUpMaterial;
    private Material playerMaterial;
    // Start is called before the first frame update
    void Start()
    {
        playerMaterial = player.GetComponent<Renderer>().material;
    }

    private void OnTriggerEnter(Collider other)
    {
        StartCoroutine(startPowerUp());
    }

    IEnumerator startPowerUp()
    {
        player.jumpPower = 600;
        player.gameObject.GetComponent<Renderer>().material = powerUpMaterial;
        yield return new WaitForSeconds(5);
        player.GetComponent<Renderer>().material = playerMaterial;
        player.jumpPower = 300;
    }


}
